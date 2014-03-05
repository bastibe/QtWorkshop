#ifndef TIME_H
#define TIME_H

#include <QQuickItem>
#include <QDateTime>
#include <QTimer>

class Time : public QQuickItem
{
    Q_OBJECT
    Q_DISABLE_COPY(Time)
    Q_PROPERTY(int second READ second NOTIFY secondChanged)
    Q_PROPERTY(int minute READ minute NOTIFY minuteChanged)
    Q_PROPERTY(int hour READ hour NOTIFY hourChanged)

public:
    Time(QQuickItem *parent = 0);
    ~Time();

    int second() { return m_second; }
    int minute() { return m_minute; }
    int hour() { return m_hour; }

signals:
    void secondChanged(int second);
    void minuteChanged(int minute);
    void hourChanged(int hour);

private slots:
    void timerFired();

private:
    QTimer m_timer;
    int m_second;
    int m_minute;
    int m_hour;
};

#endif // TIME_H

