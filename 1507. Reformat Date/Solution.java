class Solution {
    public String reformatDate(String date) {
        String day = date.substring(0,2);    //get the first 2 chars from input

        if(!Character.isDigit(day.charAt(1))){   //check if the second char is a letter or a digit 
        //i.e., if the date is in the range 1-9 then second char is not a digit. 
        //If it is in the range 10-31, then second char is a digit and this test fails

        day = date.substring(0,1);  //if the date is in range 1-9, then update day to contain only numbers and no letters that follows number

        }

        if(day.length() == 1){    //if the day is in the range 1-9, then modify the day to be in the format 01-09
            day = "0" + day; 
        }

        String[] input = date.split(" ");  //split the input to easily access year and month

        String month = input[1]; 
        String m = "";   //use switch case or map to assign corresponding month number to m

        switch(month){
            case "Jan":
                m = "01";
                break;
            case "Feb":
                m = "02";
                break;
            case "Mar":
                m = "03";
                break;
            case "Apr":
                m = "04";
                break;
            case "May":
                m = "05";
                break;
            case "Jun":
                m = "06";
                break;
            case "Jul":
                m = "07";
                break;
            case "Aug":
                m = "08";
                break;
            case "Sep":
                m = "09";
                break;
            case "Oct":
                m = "10";
                break;
            case "Nov":
                m = "11";
                break;
            case "Dec":
                m = "12";
                break;

        }

         String y = input[2]; //get the year. No modifications needed on year as we are using the YYYY format

        //create a stringbuilder and append the year, m and day and return as result

        StringBuilder res = new StringBuilder(y);
        res.append("-");
        res.append(m);
        res.append("-");
        res.append(day);
        return res.toString();
    }
}