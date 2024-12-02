def binary_string_without_consecutive_ones(n):

    
    def generate_strings(n, current_string):
        if n == 0:
            result.append(current_string)
            return
        
        # 总是可以添加 '0'
        generate_strings(n - 1, current_string + '0')
        
        # 仅当 current_string 的最后一个字符不是 '1' 时添加 '1'
        if not current_string or current_string[-1] != '1':
            generate_strings(n - 1, current_string + '1')

    result = []
    generate_strings(n, '')
    return result







if __name__=="__main__":
    n = 3
    binary_string = []
    print(binary_string_without_consecutive_ones(n))
    n = 4
    binary_string = []
    print(binary_string_without_consecutive_ones(n))
    