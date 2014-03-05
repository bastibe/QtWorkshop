#ifndef COUNTER_H
#define COUNTER_H

#include <QQuickItem>

class Counter : public QQuickItem
{
    Q_OBJECT
    Q_DISABLE_COPY(Counter)
    Q_PROPERTY(int value READ value WRITE setValue NOTIFY valueChanged)

public:
    Counter(QQuickItem *parent = 0);
    ~Counter();

    int value();

public slots:
    void setValue(int value);
    void increment();

signals:
    void valueChanged(int value);

private:
    int m_value;
};

#endif // COUNTER_H

