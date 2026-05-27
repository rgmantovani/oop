#include <iostream>
#include <memory>
#include <string>

// ── 1. Produto base (interface) ───────────────────────────
class Notifier {
public:
    virtual void send(const std::string& msg) const = 0;
    virtual ~Notifier() = default;
};

// ── 2. Produtos concretos ─────────────────────────────────
class EmailNotifier : public Notifier {
public:
    void send(const std::string& msg) const override {
        std::cout << "[EMAIL] " << msg << "\n";
    }
};

class SMSNotifier : public Notifier {
public:
    void send(const std::string& msg) const override {
        std::cout << "[SMS]   " << msg << "\n";
    }
};

// ── 3. Creator abstrato ───────────────────────────────────
//    Define o factory method e a lógica de negócio.
//    A lógica (notify) nunca sabe qual Notifier será usado.
class NotificationService {
public:
    // Factory Method — subclasse decide o produto
    virtual std::unique_ptr<Notifier> createNotifier() const = 0;

    // Lógica de negócio usa o factory method
    void notify(const std::string& msg) const {
        auto notifier = createNotifier();
        notifier->send(msg);
    }

    virtual ~NotificationService() = default;
};

// ── 4. Creators concretos ─────────────────────────────────
class EmailService : public NotificationService {
public:
    std::unique_ptr<Notifier> createNotifier() const override {
        return std::make_unique<EmailNotifier>();
    }
};

class SMSService : public NotificationService {
public:
    std::unique_ptr<Notifier> createNotifier() const override {
        return std::make_unique<SMSNotifier>();
    }
};

// ── 5. Main ───────────────────────────────────────────────
int main() {
    // O código abaixo não sabe nada sobre Email ou SMS —
    // só fala com NotificationService (tipo abstrato).
    NotificationService* services[] = {
        new EmailService(),
        new SMSService(),
    };

    for (auto* svc : services) {
        svc->notify("Sua senha foi alterada.");
        delete svc;
    }

    return 0;
}