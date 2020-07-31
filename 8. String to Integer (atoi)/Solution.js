var myAtoi = function (str) {
    let match = str.match(/^\s*[-+]?\d+/);
    if (match === null) return 0;
    let to_return = parseInt(match.join(""));
    if (to_return > 2147483647) return 2147483647;
    if (to_return < -2147483648) return -2147483648;
    return to_return;
};
