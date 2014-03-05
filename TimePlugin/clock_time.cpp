#include "clock_time.h"

Time::Time(QQuickItem *parent):
    QQuickItem(parent),
    m_timer(parent)
{
    QTime currentTime = QDateTime::currentDateTime().time();
    m_second = currentTime.second();
    m_minute = currentTime.minute();
    m_hour = currentTime.hour();
    m_timer.setInterval(50);
    connect(&m_timer, SIGNAL(timeout()), this, SLOT(timerFired()));
    m_timer.start();
}

Time::~Time()
{
}

void Time::timerFired()
{
    QTime currentTime = QDateTime::currentDateTime().time();
    if (currentTime.second() != m_second) {
        m_second = currentTime.second();
        emit secondChanged(m_second);
    }
    if (currentTime.minute() != m_minute) {
        m_minute = currentTime.minute();
        emit minuteChanged(m_minute);
    }
    if (currentTime.hour() != m_hour) {
        m_hour = currentTime.hour();
        emit hourChanged(m_hour);
    }
}

