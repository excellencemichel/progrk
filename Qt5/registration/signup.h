#ifndef SIGNUP_H
#define SIGNUP_H

#include <QDialog>

namespace Ui {
class DialogSignup;
}

class DialogSignup : public QDialog
{
    Q_OBJECT

public:
    explicit DialogSignup(QWidget *parent = 0);
    ~DialogSignup();

private:
    Ui::DialogSignup *ui;
};

#endif // SIGNUP_H
