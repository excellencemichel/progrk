#ifndef LOGGEDIN_H
#define LOGGEDIN_H

#include <QMainWindow>

namespace Ui {
class Loggedin;
}

class Loggedin : public QMainWindow
{
    Q_OBJECT

public:
    explicit Loggedin(QWidget *parent = 0);
    ~Loggedin();

private:
    Ui::Loggedin *ui;
};

#endif // LOGGEDIN_H
