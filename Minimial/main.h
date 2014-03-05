#ifndef MAIN_H
#define MAIN_H

#include <QObject>

class Counter : public QObject {
    Q_OBJECT
    Q_PROPERTY(int value READ value WRITE setValue NOTIFY valueChanged)

public:
    Counter();
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

#endif // MAIN_H
