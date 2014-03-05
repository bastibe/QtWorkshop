#ifndef TIME_PLUGIN_H
#define TIME_PLUGIN_H

#include <QQmlExtensionPlugin>

class TimePlugin : public QQmlExtensionPlugin
{
    Q_OBJECT
    Q_PLUGIN_METADATA(IID "org.qt-project.Qt.QQmlExtensionInterface")

public:
    void registerTypes(const char *uri);
};

#endif // TIME_PLUGIN_H

