import './main.scss';
import { carouselInit, CarouselSlider } from "./animations/carousel";
import './ts/_animations';
import './ts/_lenis';
import './ts/_infiniteScroler';

declare const homepage:boolean

function handleScroll(): void {
    const nav = document.querySelector('nav.nav') as HTMLElement | null;
    if (!nav) return;

    let lastScrollTop = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;

        if (currentScroll === 0) {
            nav.classList.remove('hide');
        } else if (currentScroll > lastScrollTop) {
            nav.classList.add('hide');
        } else if (currentScroll > 100 && currentScroll < lastScrollTop) {
            nav.classList.remove('hide');
        }

        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
    });
}

window.addEventListener('load', init);

function init() {
    handleScroll()
    runCarousel()
}


function runCarousel() {
    try {
        if (homepage) {
            // Carousel.switchSlides()
            carouselInit()
            CarouselSlider.switchSlides()
            setInterval(CarouselSlider.switchSlides, 20000)
        }
    } catch (error) {
        return
    }
}
