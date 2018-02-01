def order_my_list(values,order="n"):

    def isorder():
        return order == "r"

    for v in sorted(values, reverse=1):
        print(v)


nums = [12,25,65,14,36,98]

order_my_list(nums)

