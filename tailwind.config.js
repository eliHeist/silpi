module.exports = {
    content: ['../templates/*.html', '../**/templates/**/*.html'],
    darkMode: 'media', // or 'class'
    theme: {
        extend: {
            colors: {
                'primary': {
                    50: 'rgb(200, 251, 251)',
                    100: 'rgb(146, 238, 238)',
                    200: 'rgb(100, 219, 219)',
                    300: 'rgb(61, 201, 201)',
                    400: 'rgb(27, 184, 184)',
                    500: 'rgb(0, 175, 175)',
                    600: 'rgb(0, 142, 142)',
                    700: 'rgb(0, 118, 118)',
                    800: 'rgb(0, 54, 54)',
                    900: 'rgb(0, 33, 33)',
                },
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
                body: ['Poppins', 'sans-serif']
            },
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
};
