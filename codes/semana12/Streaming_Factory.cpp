#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <random>
#include <map>
#include <functional>

// ── Track ────────────────────────────────────────────────
struct Track {
    std::string name;
    std::string artist;
    std::string genre;
};

// ── Strategy: RecommendationEngine ───────────────────────
class RecommendationEngine {
public:
    virtual std::vector<Track> recommend(
        const std::vector<Track>& history) const = 0;
    virtual ~RecommendationEngine() = default;
};

// Spotify: recomenda pelo gênero mais ouvido
class SpotifyEngine : public RecommendationEngine {
public:
    std::vector<Track> recommend(
        const std::vector<Track>& history) const override
    {
        // Conta gêneros
        std::map<std::string,int> freq;
        for (const auto& t : history) ++freq[t.genre];
        auto it = std::max_element(freq.begin(), freq.end(),
            [](const auto& a, const auto& b){
                return a.second < b.second; });
        std::string top = it->first;

        std::vector<Track> result;
        for (const auto& t : history)
            if (t.genre == top) result.push_back(t);
        return result;
    }
};

// Apple Music: recomenda pelo artista mais ouvido
class AppleMusicEngine : public RecommendationEngine {
public:
    std::vector<Track> recommend(
        const std::vector<Track>& history) const override
    {
        std::map<std::string,int> freq;
        for (const auto& t : history) ++freq[t.artist];
        auto it = std::max_element(freq.begin(), freq.end(),
            [](const auto& a, const auto& b){
                return a.second < b.second; });
        std::string top = it->first;

        std::vector<Track> result;
        for (const auto& t : history)
            if (t.artist == top) result.push_back(t);
        return result;
    }
};

// Deezer: embaralha e retorna os 3 primeiros
class DeezerEngine : public RecommendationEngine {
public:
    std::vector<Track> recommend(
        const std::vector<Track>& history) const override
    {
        auto shuffled = history;
        std::shuffle(shuffled.begin(), shuffled.end(),
                     std::mt19937{std::random_device{}()});
        if (shuffled.size() > 3) shuffled.resize(3);
        return shuffled;
    }
};

// ── Creator abstrato: MusicPlatform ──────────────────────
class MusicPlatform {
    // Bônus: cache — chave = hash simples do histórico
    mutable std::string          _cacheKey;
    mutable std::vector<Track>   _cache;

    std::string hashHistory(
        const std::vector<Track>& h) const
    {
        std::string key;
        for (const auto& t : h) key += t.name + "|";
        return key;
    }

public:
    // Factory Method
    virtual std::unique_ptr<RecommendationEngine>
        createEngine() const = 0;

    virtual std::string platformName() const = 0;

    void getPlaylist(const std::vector<Track>& history) {
        auto key = hashHistory(history);
        if (key == _cacheKey) {
            std::cout << "[cache hit] ";
        } else {
            _cacheKey = key;
            _cache    = createEngine()->recommend(history);
        }
        std::cout << "=== " << platformName()
                  << " — Playlist ===\n";
        for (const auto& t : _cache)
            std::cout << "  " << t.name
                      << " — " << t.artist << "\n";
        std::cout << "\n";
    }

    virtual ~MusicPlatform() = default;
};

// ── Creators concretos ───────────────────────────────────
class SpotifyPlatform : public MusicPlatform {
public:
    std::unique_ptr<RecommendationEngine>
    createEngine() const override {
        return std::make_unique<SpotifyEngine>();
    }
    std::string platformName() const override {
        return "Spotify"; }
};

class AppleMusicPlatform : public MusicPlatform {
public:
    std::unique_ptr<RecommendationEngine>
    createEngine() const override {
        return std::make_unique<AppleMusicEngine>();
    }
    std::string platformName() const override {
        return "Apple Music"; }
};

class DeezerPlatform : public MusicPlatform {
public:
    std::unique_ptr<RecommendationEngine>
    createEngine() const override {
        return std::make_unique<DeezerEngine>();
    }
    std::string platformName() const override {
        return "Deezer"; }
};

// ── Main ─────────────────────────────────────────────────
int main() {
    std::vector<Track> history = {
        {"Blinding Lights",    "The Weeknd",  "Pop"},
        {"Starboy",            "The Weeknd",  "Pop"},
        {"Save Your Tears",    "The Weeknd",  "Pop"},
        {"Bohemian Rhapsody",  "Queen",       "Rock"},
        {"Back in Black",      "AC/DC",       "Rock"},
        {"Hotel California",   "Eagles",      "Rock"},
        {"Shape of You",       "Ed Sheeran",  "Pop"},
        {"Bad Guy",            "Billie Eilish","Pop"},
    };

    std::vector<std::unique_ptr<MusicPlatform>> platforms;
    platforms.push_back(std::make_unique<SpotifyPlatform>());
    platforms.push_back(std::make_unique<AppleMusicPlatform>());
    platforms.push_back(std::make_unique<DeezerPlatform>());

    for (auto& p : platforms) {
        p->getPlaylist(history);
        // Segunda chamada → deve usar cache (Spotify/Apple)
        p->getPlaylist(history);
    }
    return 0;
}