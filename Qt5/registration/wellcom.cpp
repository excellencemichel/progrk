#include "loggedin.h"
#include "ui_loggedin.h"

Loggedin::Loggedin(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Loggedin)
{
    ui->setupUi(this);
}

Loggedin::~Loggedin()
{
    delete ui;
}
