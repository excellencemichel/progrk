#ifndef OTHER1_H
#define OTHER1_H

#include <QMainWindow>

namespace Ui {
class Other1;
}

class Other1 : public QMainWindow
{
    Q_OBJECT

public:
    explicit Other1(QWidget *parent = 0);
    ~Other1();

private:
    Ui::Other1 *ui;
};

#endif // OTHER1_H
