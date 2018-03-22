#ifndef OTHERWINDOW_H
#define OTHERWINDOW_H

#include <QMainWindow>

namespace Ui {
class otherwindow;
}

class otherwindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit otherwindow(QWidget *parent = 0);
    ~otherwindow();

private:
    Ui::otherwindow *ui;
};

#endif // OTHERWINDOW_H
