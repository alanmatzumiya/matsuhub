if (!(function f() {}).name) {
    Object.defineProperty(Function.prototype, 'name', {
        get: function() {
            var match = this.toString().match(/^function\s*([^\s(]+)/);
            var name = Array.isArray(match) && match[1] ? match[1] : "";
            Object.defineProperty(this, 'name', { value: name });
            return name;
        }
    });
}
