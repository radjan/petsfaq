#include <iostream>
#include <cmath>
#include <unistd.h>

double ConvertDegreeToRadians(double degrees)
{
    return (M_PI/180)*degrees;
}

double GetDistance(double Lat1, double Long1, double Lat2, double Long2)
{
    double Lat1r = ConvertDegreeToRadians(Lat1);
    double Lat2r = ConvertDegreeToRadians(Lat2);
    double Long1r = ConvertDegreeToRadians(Long1);
    double Long2r = ConvertDegreeToRadians(Long2);

    double R = 6371; // Earth's radius (km)
    double d = acos(sin(Lat1r) *
            sin(Lat2r) + cos(Lat1r) *
            cos(Lat2r) *
            cos(Long2r-Long1r)) * R;
    return d;
}

int main()
{
    double x1=0;
    double y1=0;
    double x2=1;
    double y2=1;
    double offset=0.01; // 1degree

    double distance=1; // 1km
    double tmp_d=0;

    double pre = -1;
    double now = -1;
    double ratio = 1;

    while (1)
    {
        offset *= ratio;
        //x2 += now*offset;
        y2 += now*offset;
        ratio = 1;
        //tmp_d = GetDistance(x1,0,x2,0);
        tmp_d = GetDistance(0,y1,0,y2);
        if ((pre == now) && (tmp_d < distance)){
            pre = now;
            now = 1;
            ratio = 1;
        }
        else if ((pre == now) && (tmp_d > distance)){
            pre = now;
            now = -1;
            ratio = 1;
        }
        else if ((pre != now) && (tmp_d < distance)){
            pre = now;
            now = 1;
            ratio = 0.1;
        }
        else if ((pre != now) && (tmp_d > distance)){
            pre = now;
            now = -1;
            ratio = 0.1;
        }
        //std::cout<<"("<<x1<<", "<<x2<<") distance: "<< tmp_d <<std::endl;
        std::cout<<"("<<y1<<", "<<y2<<") distance: "<< tmp_d <<std::endl;
        usleep(50000);
    }
    return 0;
}

// latitude offset = 0.00899322
// longitude offset = 0.00899322
