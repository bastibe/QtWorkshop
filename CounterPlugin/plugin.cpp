#include "plugin.h"
#include "counter.h"

#include <qqml.h>

void Plugin::registerTypes(const char *uri)
{
    // @uri Plugin
    qmlRegisterType<Counter>(uri, 1, 0, "Counter");
}


