#include "otherwindow.h"
#include "ui_otherwindow.h"

otherwindow::otherwindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::otherwindow)
{
    ui->setupUi(this);
}

otherwindow::~otherwindow()
{
    delete ui;
}
