module.exports = {
    content: ['../templates/*.html', '../**/templates/**/*.html'],
    darkMode: 'media', // or 'class'
    theme: {
        extend: {
            colors: {
                light: "hsl(var(--clr-light) / <alpha-value>)",
                muted: "hsl(var(--clr-muted) / <alpha-value>)",
                primary: "hsl(var(--clr-primary) / <alpha-value>)",
                secondary: "hsl(var(--clr-secondary) / <alpha-value>)",
                dark: "hsl(var(--clr-dark) / <alpha-value>)",
                grey: {
                    50: 'rgb(252, 252, 252)',
                    100: 'rgb(245, 245, 245)',
                    200: 'rgb(234, 234, 234)',
                    300: 'rgb(219, 219, 219)',
                    400: 'rgb(175, 175, 175)',
                    500: 'rgb(130, 130, 130)',
                    600: 'rgb(97, 97, 97)',
                    700: 'rgb(69, 69, 69)',
                    800: 'rgb(42, 42, 42)',
                    900: 'rgb(28, 28, 28)'
                }
            },
            fontFamily: {
                body: ['Lato', 'sans-serif']
            },
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
};
