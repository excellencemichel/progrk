#ifndef DATA_WINDOW_H
#define DATA_WINDOW_H

#include <QMainWindow>

namespace Ui {
class data_Window;
}

class data_Window : public QMainWindow
{
    Q_OBJECT

public:
    explicit data_Window(QWidget *parent = 0);
    ~data_Window();

private:
    Ui::data_Window *ui;
};

#endif // DATA_WINDOW_H
