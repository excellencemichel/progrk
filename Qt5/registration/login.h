#ifndef DIALOGREGISTRATION_H
#define DIALOGREGISTRATION_H

#include <QDialog>

namespace Ui {
class DialogRegistration;
}

class DialogRegistration : public QDialog
{
    Q_OBJECT

public:
    explicit DialogRegistration(QWidget *parent = 0);
    ~DialogRegistration();

private:
    Ui::DialogRegistration *ui;
};

#endif // DIALOGREGISTRATION_H
