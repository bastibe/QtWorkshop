#include "counter.h"

Counter::Counter(QQuickItem *parent):
    QQuickItem(parent)
{
    // By default, QQuickItem does not draw anything. If you subclass
    // QQuickItem to create a visual item, you will need to uncomment the
    // following line and re-implement updatePaintNode()

    // setFlag(ItemHasContents, true);
}

Counter::~Counter()
{
}

int Counter::value() {
    return m_value;
}

void Counter::setValue(int value) {
    if (value != m_value) {
        m_value = value;
        emit valueChanged(value);
        qDebug() << m_value;
    }
}

void Counter::increment() {
    this->setValue(m_value+1);
}
