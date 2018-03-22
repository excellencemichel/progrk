#include "number.h"
#include "ui_number.h"

Number::Number(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Number)
{
    ui->setupUi(this);
}

Number::~Number()
{
    delete ui;
}
