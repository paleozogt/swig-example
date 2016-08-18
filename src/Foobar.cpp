#include "Foobar.hpp"

Foobar::Foobar(int val) : val(val) {
}

Foobar::~Foobar() {
}

int Foobar::get() {
    return val;
}

void Foobar::set(int val) {
    this->val= val;
}