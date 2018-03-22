#include "signup.h"
#include "ui_signup.h"

DialogSignup::DialogSignup(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogSignup)
{
    ui->setupUi(this);
}

DialogSignup::~DialogSignup()
{
    delete ui;
}
