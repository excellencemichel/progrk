#include "other1.h"
#include "ui_other1.h"

Other1::Other1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Other1)
{
    ui->setupUi(this);
}

Other1::~Other1()
{
    delete ui;
}
