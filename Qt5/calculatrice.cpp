#include "calculatrice.h"
#include "ui_calculatrice.h"

calculatrice::calculatrice(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::calculatrice)
{
    ui->setupUi(this);
}

calculatrice::~calculatrice()
{
    delete ui;
}
