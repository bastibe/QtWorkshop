#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QWindow>
#include <QIcon>
#include <QTranslator>
#include <QDebug>
#include <QtQml>
#include "main.h"

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);
    QTranslator translator;
    translator.load("german");
    app.installTranslator(&translator);
    qmlRegisterType<Counter>("Backend", 1, 0, "Counter");
    QQmlApplicationEngine engine("main.qml");
    if (engine.rootObjects().length() > 0) {
        QWindow *mainWindow = (QWindow*)engine.rootObjects()[0];
        mainWindow->setVisible(true);
        mainWindow->setIcon(QIcon("Logo.png"));
    }
    return app.exec();
}


Counter::Counter()
{
    m_value = 0;
}


Counter::~Counter()
{
}


int Counter::value()
{
    return m_value;
}


void Counter::setValue(int value)
{
    if (m_value != value) {
        m_value = value;
        emit valueChanged(m_value);
    }
}


void Counter::increment()
{
    setValue(m_value+1);
}
