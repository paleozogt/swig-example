#pragma once

class Foobar {
public:
    Foobar(int val= 0);
    virtual ~Foobar();

    virtual int get();
    virtual void set(int val);

protected:
    int val;
};
