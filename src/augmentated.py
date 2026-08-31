import os
import cv2
import random
import numpy as np

def resize_image(img):
    return cv2.resize(img, (224, 224))

def rotate_image(img):
    angle=random.uniform(-10, 10)
    h, w=img.shape[:2]
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
    return cv2.warpAffine(
        img,
        M,
        (w, h),
        borderMode=cv2.BORDER_REPLICATE
    )


def brightness(img):
    alpha=random.uniform(0.9, 1.1)
    beta=random.randint(-10, 10)

    img=cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return img

def gaussian_noise(img):
    noise=np.random.normal(0,8, img.shape).astype(np.int16)
    noisy=img.astype(np.int16) + noise
    noisy=np.clip(noisy, 0, 255)

    return noisy.astype(np.uint8)

def zoom(img):
    scale=random.uniform(0.95, 1.05)
    h, w=img.shape[:2]
    nh=int(h * scale)
    nw=int(w* scale)

    resized=cv2.resize(img, (nw, nh))

    if scale >1:
        startx=(nw-w)//2
        starty=(nh- h)//2

        return resized[starty:starty+h, startx:startx+w]
    else:
        result=np.zeros((h,w), dtype=np.uint8)

        x=(w-nw)//2
        y=(h-nh)//2

        result[y:y+nh, x:x+nw]= resized
    return result

def shift(img):
    h, w=img.shape[:2]
    tx=random.randint(-10,10)
    ty=random.randint(-10, 10)

    M=np.float32([[1,0,tx],
                  [0,1,ty]])
    
    return cv2.warpAffine(
        img, M, (w,h), borderMode=cv2.BORDER_REPLICATE
    )

def augment_balance(base_path, categories, num_images):
    transformations={
        "rotate":rotate_image,
        "brightness":brightness,
        "noise":gaussian_noise,
        "zoom":zoom,
        "shift":shift
    }
    for category in categories:
        image_path=os.path.join(base_path, category)
        images=[
            os.path.join(image_path, img)
            for img in os.listdir(image_path)
        ]
        i=1
        while i<=num_images:
            image=random.choice(images)

            try:
                original=cv2.imread(image, cv2.IMREAD_GRAYSCALE)
                original=resize_image(original)

                transformed=original.copy()
                num_transform=random.randint(1,3)
                selected=random.sample(
                    list(transformations.keys()),
                    num_transform
                )

                for key in selected :
                    transformed=transformations[key](transformed)
                
                save_path=os.path.join(
                    image_path,
                    f"aug_{category}_{i}.png"
                )
                cv2.imwrite(save_path, transformed)
                i+=1
            except Exception as e:
                print(e)
                continue