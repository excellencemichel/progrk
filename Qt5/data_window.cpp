#include "data_window.h"
#include "ui_data_window.h"

data_Window::data_Window(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::data_Window)
{
    ui->setupUi(this);
}

data_Window::~data_Window()
{
    delete ui;
}
