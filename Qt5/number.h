#ifndef NUMBER_H
#define NUMBER_H

#include <QMainWindow>

namespace Ui {
class Number;
}

class Number : public QMainWindow
{
    Q_OBJECT

public:
    explicit Number(QWidget *parent = 0);
    ~Number();

private:
    Ui::Number *ui;
};

#endif // NUMBER_H
