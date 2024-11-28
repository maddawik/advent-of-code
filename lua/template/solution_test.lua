local runner = require("util.test_runner")
local solution = require("template.solution") -- TODO: Update this to "20XX.dayXX.solution"

runner:test(function()
	local got = solution.Part1()
	local want = 0
	assert(got == want, "Part 1 failed, " .. got .. " is not equal to " .. want)
end)

runner:test(function()
	local got = solution.Part2()
	local want = 0
	assert(got == want, "Part 2 failed, " .. got .. " is not equal to " .. want)
end)

runner:evaluate()
