#ifndef MICHEL_H
#define MICHEL_H

#include <QMainWindow>

namespace Ui {
class Michel;
}

class Michel : public QMainWindow
{
    Q_OBJECT

public:
    explicit Michel(QWidget *parent = 0);
    ~Michel();

private:
    Ui::Michel *ui;
};

#endif // MICHEL_H
