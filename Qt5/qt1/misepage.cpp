#include "misepage.h"
#include "ui_misepage.h"

MisePage::MisePage(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MisePage)
{
    ui->setupUi(this);
}

MisePage::~MisePage()
{
    delete ui;
}
