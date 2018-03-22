#ifndef GROUPBOX_H
#define GROUPBOX_H

#include <QGroupBox>

namespace Ui {
class GroupBox;
}

class GroupBox : public QGroupBox
{
    Q_OBJECT

public:
    explicit GroupBox(QWidget *parent = 0);
    ~GroupBox();

private:
    Ui::GroupBox *ui;
};

#endif // GROUPBOX_H
