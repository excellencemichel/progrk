#include "selectingdata.h"
#include "ui_selectingdata.h"

SelectingData::SelectingData(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::SelectingData)
{
    ui->setupUi(this);
}

SelectingData::~SelectingData()
{
    delete ui;
}
