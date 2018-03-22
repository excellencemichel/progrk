#include "sow.h"
#include "ui_sow.h"

sow::sow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::sow)
{
    ui->setupUi(this);
}

sow::~sow()
{
    delete ui;
}
