QT      += core qml
TARGET   = Minimal
TEMPLATE = app
TRANSLATIONS += german.ts

macx {
    QmlFiles.path = Contents/MacOS
    QmlFiles.files = $$files(*.qml)
    QMAKE_BUNDLE_DATA += QmlFiles
}

SOURCES += \
    main.cpp

OTHER_FILES += \
    main.qml

lupdate_only {
    SOURCES += *.qml
}

HEADERS += \
    main.h
