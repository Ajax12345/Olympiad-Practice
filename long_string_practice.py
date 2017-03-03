the_string = "v@aksrc$f0qokxs#4hil#0rcgs6u7fzkbw348#39mi#yochz#oj1z7$p5yjnbije9c1ip3bz$gstiu?3pgw10wfu#5nux68nxjd0plybdeo#oe1bsbw08pxwwt0gfp0ufs@32yh?pnczny3zascshj3wiuomjft15i?ta9so0etum26qpj#ympkz7wnovxh9cwqh8vxobt$#uvzm4vmq1@zy?04b@oqx4kb#8?s#un?59f7?3kyikl@7p1l3hr1gl@70kh0mf@2bb9dpe0p8rchm#7@?261yyvyymipp#jbfh68byx7xae8o@@n@i1#57i4cqze5zpde?xrv#cwmisqhw?qfe05pa30lt1?kr57htsz5?ld4mxqlhq1t49041p@kagnk3?v7#l@c#rk3trxi80a?hnhbxx8x#6k8#0e78uy?lqhxpkwzcik5?p0n1do2bkyidt7u?wln1qe#x?xfweb359bi$hwa2aagn8#tkf2fq7av6qmgztkzjj#mbmj8cgsuwjz9wf@35akotjr$a9pk08t$@q@f9n#7uauuk@#azlsqxkwg0vltuqsj8dxpc1dpalflt2$s5f9cjkocg38en$ep9i0i5hxz@r#spizhovbowdy9l7q2m9?2"
primes = []
composites = []
generated_string = []
numeric_counter = 0
for i in the_string:
    try:
        the_number = int(i)
        the_primes = [x for x in range(2, the_number+1) if all(x%y != 0 for y in range(2, x))]
        if the_number in the_primes:
            primes.append(the_number)

        else:
            composites.append(the_number)




    except:
        if numeric_counter < 25:
            the_value = ord(i)+1
            the_new_character = chr(the_value)
            generated_string.append(the_new_character)
            numeric_counter += 1

        else:
            continue


the_final_string = ''.join(generated_string)
final_product = sum(primes)*sum(composites)
print the_final_string + str(final_product)
