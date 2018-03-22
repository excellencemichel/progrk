#include "michel.h"
#include "ui_michel.h"

Michel::Michel(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Michel)
{
    ui->setupUi(this);
}

Michel::~Michel()
{
    delete ui;
}
