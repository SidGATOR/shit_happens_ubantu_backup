proc max {arg1 arg2} {
    if {$arg1 > $arg2} {
        set x $arg1
        return $x
    } else {
        set x $arg2
        return $x
    }
}

puts "[max 4 7] is greater"
