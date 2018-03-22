#include "dataliste.h"
#include "ui_dataliste.h"

Dataliste::Dataliste(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Dataliste)
{
    ui->setupUi(this);
}

Dataliste::~Dataliste()
{
    delete ui;
}
