#include "insertdatafromdtdgn.h"
#include "ui_insertdatafromdtdgn.h"

insertDataFromDtDgn::insertDataFromDtDgn(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::insertDataFromDtDgn)
{
    ui->setupUi(this);
}

insertDataFromDtDgn::~insertDataFromDtDgn()
{
    delete ui;
}
