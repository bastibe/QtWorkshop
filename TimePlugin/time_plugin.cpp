#include "time_plugin.h"
#include "clock_time.h"

#include <qqml.h>

void TimePlugin::registerTypes(const char *uri)
{
    // @uri ClockTime
    qmlRegisterType<Time>(uri, 1, 0, "Time");
}


