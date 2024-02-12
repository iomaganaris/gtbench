#include <string>

#include "nvToolsExt.h"

struct ProfileMarker {
    std::string range_name;
    explicit ProfileMarker(const char* range_name) : range_name(range_name) {
        nvtxRangePush(range_name);
    }
    ~ProfileMarker() {
        nvtxRangePop();
    }
};
