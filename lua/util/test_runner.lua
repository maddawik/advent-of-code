local M = {
	hasErrors = false,
}

function M:test(fun)
	local status, err = pcall(fun)
	if not status then
		self.hasErrors = true
		print(err)
	end
end

function M:evaluate()
	if self.hasErrors then
		print("Test suite completed with errors")
		os.exit(1)
	else
		print("Test suite completed successfully!")
	end
end

return M
