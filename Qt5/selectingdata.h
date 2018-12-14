#ifndef SELECTINGDATA_H
#define SELECTINGDATA_H

#include <QMainWindow>

namespace Ui {
class SelectingData;
}

class SelectingData : public QMainWindow
{
    Q_OBJECT

public:
    explicit SelectingData(QWidget *parent = 0);
    ~SelectingData();

private:
    Ui::SelectingData *ui;
};

#endif // SELECTINGDATA_H
