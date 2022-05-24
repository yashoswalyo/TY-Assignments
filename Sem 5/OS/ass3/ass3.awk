BEGIN	{
    sum = 0
    avg = 0
    FS = "|"
}
{
    sum = $3+$4+$5+$6+$7;
    avg = sum/5;
    if (avg>90) {
        grade = "O";
    } else if (avg > 80) {
        grade = "A+";
    } else if (avg > 70) {
        grade = "A";
    } else if (avg > 60) {
        grade = "B+";
    } else if (avg > 50) {
        grade = "B";
    } else if (avg > 40) {
        grade = "C";
    } else if (avg > 35) {
        grade = "P";
    }
    printf $1"|"avg"|"grade"\n";
}
