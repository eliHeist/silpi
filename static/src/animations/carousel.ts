import { gsap } from "gsap"
import { Expo } from "gsap/all"

let carousel:HTMLDivElement = document.getElementById('carouselSlides') as HTMLDivElement
let carouselslides:NodeListOf<HTMLDivElement> = document.querySelectorAll<HTMLDivElement>('#carouselSlides .carouselSlide')
let carouselslideLength:number = carouselslides.length - 1
let carouselcurrentSlide:number = -1


export class CarouselSlider {
    // method to show the slide
    static showSlide(num:number) {
        // showing next slide
        const timeline1 = gsap.timeline({
            paused: true,
            defaults: {
                Easings: Expo.easeOut
            }
        }).to(carouselslides[carouselcurrentSlide], {
            clipPath: 'polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)',
            duration: 0.9
        }, '+=.7').to(carouselslides[carouselcurrentSlide].querySelectorAll('.content > *'), {
            clipPath: 'polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)',
            duration: 0.4,
            stagger: 0.15
        }, '+=.5')
        timeline1.play()
    }
    // method to hide the slide
    static hideSlide(num:number) {
        // hiding previous slide
        const timeline2 = gsap.timeline({
            paused: true,
            defaults: {
                Easings: Expo.easeInOut
            }
        }).to(carouselslides[carouselcurrentSlide].querySelectorAll('.content > *'), {
            clipPath: 'polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%)',
            duration: 0.4,
            stagger: 0.15
        }).to(carouselslides[carouselcurrentSlide], {
            clipPath: 'polygon(100% 0%, 100% 0%, 100% 100%, 100% 100%)',
            duration: 0.6,
            delay: 2
        }, '+=1')
        timeline2.play()
    }
    static nextSlide() {
        if (carouselcurrentSlide == carouselslideLength) {
            return carouselcurrentSlide = 0
        } else {
            return ++carouselcurrentSlide
        }
    }
    static switchSlides() {
        if (carouselcurrentSlide >= 0) {
            CarouselSlider.hideSlide(carouselcurrentSlide)
            CarouselSlider.showSlide(CarouselSlider.nextSlide())
        }
        else {
            CarouselSlider.showSlide(CarouselSlider.nextSlide())
        }
    }
}

// set the slides initially
export function carouselInit() {
    carouselslides.forEach(slide => {
        gsap.set(slide.querySelectorAll('.content > *'), {
            clipPath: 'polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%)'
        })
        gsap.set(slide, {
            clipPath: 'polygon(0% 0%, 0% 0%, 0% 100%, 0% 100%)'
        })
    });
}