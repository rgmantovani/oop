#include <vector>
#include <string>

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

class DigitalImage {
    private:
        int width, height, channels;
        unsigned char* data; // Pointer to pixel data

    public:
        // Constructor
        DigitalImage(int w, int h, int ch) : width(w), height(h), channels(ch) {
            data = new unsigned char[width * height * channels];
        }
        
        // Destructor
        ~DigitalImage() {
            delete[] data;
        }

        // Methods
        // Load image from disk
        bool load(const std::string& filename) {
            int w, h, c;
            // Force 3 channels (RGB) for simplicity
            unsigned char* img_data = stbi_load(filename.c_str(), &w, &h, &c, 3);
            if (!img_data) return false;

            width = w; height = h; channels = 3;
            data.assign(img_data, img_data + (w * h * 3)); // Copy to vector
            stbi_image_free(img_data); // Free the raw pointer
            return true;
        }

        // Save image as PNG
        bool savePNG(const std::string& filename) {
            // use .data() to pass the vector's internal pointer
            return stbi_write_png(filename.c_str(), width, height, channels, data.data(), width * channels);
        }        unsigned char* getPixel(int x, int y);
};